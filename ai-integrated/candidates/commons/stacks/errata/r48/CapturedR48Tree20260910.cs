using System;
using System.IO;
using System.Text;
using System.Runtime.InteropServices;
using System.ComponentModel;
using System.Diagnostics;
using System.Threading;

// Successor of the inspected CapturedTeXTree20260909 guard. Never adopts PIDs.
public sealed class CapturedR48Tree20260910 : IDisposable {
    [StructLayout(LayoutKind.Sequential)] struct SI {
        public uint cb; public IntPtr reserved, desktop, title;
        public uint x,y,xSize,ySize,xChars,yChars,fill,flags;
        public ushort show,cb2; public IntPtr reserved2,input,output,error;
    }
    [StructLayout(LayoutKind.Sequential)] struct PI { public IntPtr process,thread; public uint pid,tid; }
    [StructLayout(LayoutKind.Sequential)] struct BasicLimits {
        public long processTime,jobTime; public uint flags;
        public UIntPtr minWs,maxWs; public uint activeLimit; public UIntPtr affinity;
        public uint priority,scheduling;
    }
    [StructLayout(LayoutKind.Sequential)] struct IO { public ulong rOps,wOps,oOps,rBytes,wBytes,oBytes; }
    [StructLayout(LayoutKind.Sequential)] struct Limits {
        public BasicLimits basic; public IO io; public UIntPtr processMem,jobMem,peakProcess,peakJob;
    }
    [StructLayout(LayoutKind.Sequential)] struct Accounting {
        public long user,kernel,periodUser,periodKernel; public uint faults,total,active,terminated;
    }
    [DllImport("kernel32", CharSet=CharSet.Unicode, SetLastError=true)] static extern IntPtr CreateJobObject(IntPtr attrs,string name);
    [DllImport("kernel32", SetLastError=true)] static extern bool SetInformationJobObject(IntPtr job,int cls,ref Limits data,uint size);
    [DllImport("kernel32", SetLastError=true)] static extern bool QueryInformationJobObject(IntPtr job,int cls,out Accounting data,uint size,IntPtr ret);
    [DllImport("kernel32", CharSet=CharSet.Unicode, SetLastError=true)] static extern bool CreateProcess(string exe,StringBuilder cmd,IntPtr pa,IntPtr ta,bool inherit,uint flags,IntPtr env,string cwd,ref SI si,out PI pi);
    [DllImport("kernel32", SetLastError=true)] static extern bool AssignProcessToJobObject(IntPtr job,IntPtr process);
    [DllImport("kernel32", SetLastError=true)] static extern uint ResumeThread(IntPtr thread);
    [DllImport("kernel32", SetLastError=true)] static extern bool SetHandleInformation(IntPtr h,uint mask,uint flags);
    [DllImport("kernel32", SetLastError=true)] static extern bool GetExitCodeProcess(IntPtr process,out uint code);
    [DllImport("kernel32", SetLastError=true)] static extern bool TerminateJobObject(IntPtr job,uint code);
    [DllImport("kernel32", SetLastError=true)] static extern bool TerminateProcess(IntPtr process,uint code);
    [DllImport("kernel32", SetLastError=true)] static extern uint WaitForSingleObject(IntPtr handle,uint milliseconds);
    [DllImport("kernel32")] static extern bool CloseHandle(IntPtr h);
    IntPtr job,process; FileStream stdout,stderr;
    public uint Id { get; private set; }
    public bool AssignedBeforeResume { get; private set; }
    public bool CleanupCompleted { get; private set; }
    public bool TerminationRequested { get; private set; }
    public uint FinalTotalProcesses { get; private set; }
    static void Check(bool ok) { if (!ok) throw new Win32Exception(Marshal.GetLastWin32Error()); }
    public static string QuoteArgument(string argument) {
        if(argument == null) throw new ArgumentNullException("argument");
        var b = new StringBuilder("\""); int slashes=0;
        foreach(char c in argument) {
            if(c == '\\') { slashes++; continue; }
            if(c == '"') { b.Append('\\',slashes*2+1); b.Append(c); }
            else { b.Append('\\',slashes); b.Append(c); }
            slashes=0;
        }
        b.Append('\\',slashes*2); b.Append('"'); return b.ToString();
    }
    public static string JoinArguments(string[] arguments) {
        var parts=new string[arguments.Length];
        for(int i=0;i<arguments.Length;i++) parts[i]=QuoteArgument(arguments[i]);
        return String.Join(" ",parts);
    }
    public CapturedR48Tree20260910(string exe,string[] arguments,string cwd,string outPath,string errPath) {
        PI pi=new PI(); bool assigned=false;
        try {
            job=CreateJobObject(IntPtr.Zero,null); Check(job!=IntPtr.Zero);
            var limits=new Limits(); limits.basic.flags=0x2000; // KILL_ON_JOB_CLOSE; no breakaway flags.
            Check(SetInformationJobObject(job,9,ref limits,(uint)Marshal.SizeOf(typeof(Limits))));
            stdout=new FileStream(outPath,FileMode.CreateNew,FileAccess.Write,FileShare.Read);
            stderr=new FileStream(errPath,FileMode.CreateNew,FileAccess.Write,FileShare.Read);
            var si=new SI(); si.cb=(uint)Marshal.SizeOf(typeof(SI)); si.flags=0x100;
            si.output=stdout.SafeFileHandle.DangerousGetHandle(); si.error=stderr.SafeFileHandle.DangerousGetHandle();
            Check(SetHandleInformation(si.output,1,1)); Check(SetHandleInformation(si.error,1,1));
            // CREATE_SUSPENDED | CREATE_NO_WINDOW: no descendant executes before assignment.
            Check(CreateProcess(exe,new StringBuilder(QuoteArgument(exe)+" "+JoinArguments(arguments)),IntPtr.Zero,IntPtr.Zero,true,0x08000004,IntPtr.Zero,cwd,ref si,out pi));
            process=pi.process; Id=pi.pid;
            Check(AssignProcessToJobObject(job,process)); assigned=true; AssignedBeforeResume=true;
            Check(SetHandleInformation(si.output,1,0)); Check(SetHandleInformation(si.error,1,0));
            if(ResumeThread(pi.thread)==0xFFFFFFFF) throw new Win32Exception(Marshal.GetLastWin32Error());
        } catch {
            if(process!=IntPtr.Zero && !assigned) {
                Check(TerminateProcess(process,1));
                Check(WaitForSingleObject(process,0xFFFFFFFF)==0);
            }
            Dispose(); throw;
        } finally {
            if(pi.thread!=IntPtr.Zero) CloseHandle(pi.thread);
        }
    }
    Accounting ReadAccounting() {
        Accounting a; Check(QueryInformationJobObject(job,1,out a,(uint)Marshal.SizeOf(typeof(Accounting)),IntPtr.Zero)); return a;
    }
    public uint ActiveProcesses { get { return job==IntPtr.Zero ? 0 : ReadAccounting().active; } }
    public uint TotalProcesses { get { return job==IntPtr.Zero ? FinalTotalProcesses : ReadAccounting().total; } }
    public bool HasExited { get { return ActiveProcesses==0; } }
    public bool RootHasExited { get { return WaitForSingleObject(process,0)==0; } }
    public bool WaitForExit(int milliseconds) {
        var watch=Stopwatch.StartNew();
        while(!HasExited) { if(watch.ElapsedMilliseconds>=milliseconds) return false; Thread.Sleep(50); }
        return true;
    }
    public uint ExitCode {
        get {
            if(!RootHasExited) throw new InvalidOperationException("Captured root still running");
            uint value; Check(GetExitCodeProcess(process,out value)); return value;
        }
    }
    public void Dispose() {
        if(job!=IntPtr.Zero) {
            if(ActiveProcesses!=0) {
                TerminationRequested=true; Check(TerminateJobObject(job,1));
                // Safety boundary: caller must retain the mutex until this captured job reaches zero.
                while(!WaitForExit(1000)) {}
            }
            FinalTotalProcesses=ReadAccounting().total;
            CleanupCompleted=true;
            CloseHandle(job); job=IntPtr.Zero;
        }
        if(process!=IntPtr.Zero) { CloseHandle(process); process=IntPtr.Zero; }
        if(stdout!=null) {stdout.Dispose();stdout=null;}
        if(stderr!=null) {stderr.Dispose();stderr=null;}
    }
}
