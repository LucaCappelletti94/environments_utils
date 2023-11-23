"""Submodule to help provide the instruction sets available in peculiar environments."""
import subprocess
from typing import List

from environments_utils.is_os import is_macos


def get_macos_available_instructions() -> List[str]:
    """Returns the list of available instructions on macOS.

    Implementation details
    ----------------------
    This method calls the `sysctl` command to get the list of available instructions:

    ```
    sysctl -a | grep machdep.cpu.features
    ```

    which returns a string like this (on a Mac with an Intel processor):

    ```
    machdep.cpu.features: FPU VME DE PSE TSC MSR PAE MCE CX8 APIC SEP MTRR PGE MCA CMOV PAT PSE36 CLFSH DS ACPI MMX FXSR SSE SSE2 SS HTT TM PBE SSE3 PCLMULQDQ DTES64 MON DSCPL VMX EST TM2 SSSE3 FMA CX16 TPR PDCM SSE4.1 SSE4.2 x2APIC MOVBE POPCNT AES PCID XSAVE OSXSAVE SEGLIM64 TSCTMR AVX1.0 RDRAND F16C
    ```

    Raises
    ------
    NotImplementedError
        If the current OS is not macOS.
    """
    if not is_macos():
        raise NotImplementedError("This method is only implemented for macOS.")

    # Get the list of available instructions
    sysctl_output = subprocess.check_output(["sysctl", "-a"]).decode("utf-8")
    cpu_features = [line for line in sysctl_output.split("\n") if "machdep.cpu.features" in line][0]

    # Extract the list of available instructions
    available_instructions = cpu_features.split(": ")[1].split(" ")
    return available_instructions