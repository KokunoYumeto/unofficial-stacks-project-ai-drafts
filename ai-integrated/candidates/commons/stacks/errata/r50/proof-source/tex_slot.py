import ctypes
import os
import sys
from datetime import datetime, timezone

class TexSlot:
    def __init__(self, timeout_ms):
        if not 1 <= timeout_ms <= 600000:
            raise ValueError("slot wait must be between 1 and 600000 ms")
        self.timeout_ms = timeout_ms

    def __enter__(self):
        self.receipt = {"name": r"Global\InterlanguageTeXSlotV1", "platform": sys.platform}
        self.owned = False
        if os.name == "nt":
            from ctypes import wintypes
            self.kernel = ctypes.WinDLL("kernel32", use_last_error=True)
            self.kernel.CreateMutexW.argtypes = (ctypes.c_void_p, wintypes.BOOL, wintypes.LPCWSTR)
            self.kernel.CreateMutexW.restype = wintypes.HANDLE
            self.kernel.WaitForSingleObject.argtypes = (wintypes.HANDLE, wintypes.DWORD)
            self.kernel.WaitForSingleObject.restype = wintypes.DWORD
            self.kernel.ReleaseMutex.argtypes = (wintypes.HANDLE,)
            self.kernel.CloseHandle.argtypes = (wintypes.HANDLE,)
            self.handle = self.kernel.CreateMutexW(None, False, self.receipt["name"])
            if not self.handle:
                raise OSError(ctypes.get_last_error(), "CreateMutexW")
            result = self.kernel.WaitForSingleObject(self.handle, self.timeout_ms)
            if result not in (0, 0x80):
                self.kernel.CloseHandle(self.handle)
                raise RuntimeError(f"TeX slot not acquired: {result:#x}; no engine launched")
            self.owned = True
            self.receipt.update(acquisition_timeout_ms=self.timeout_ms, abandoned_mutex_recovered=result == 0x80,
                                acquired_utc=datetime.now(timezone.utc).isoformat())
        else:
            self.receipt["note"] = "Windows named mutex is not applicable on this platform."
        return self

    def __exit__(self, *_):
        if self.owned:
            try:
                if not self.kernel.ReleaseMutex(self.handle):
                    raise OSError(ctypes.get_last_error(), "ReleaseMutex")
            finally:
                self.kernel.CloseHandle(self.handle)
                self.owned = False
                self.receipt["released_utc"] = datetime.now(timezone.utc).isoformat()
