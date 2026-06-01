from pathlib import Path

from fabengine.compile_profile import CompileProfile

class gfortran_mpi_omp(CompileProfile):

    def __init__(self):
        self._fortran_compiler_version = ">12.2"
        self.check_valid_version(self.fortran_compiler(), self._version)

    @property
    def fortran_compiler(self) -> str:
        return "gfortran"

    @property
    def fortran_executable(self) -> Path:
        return Path("mpif90")

    @property
    def fortran_compile_flags_common(self) -> list[str]:
        return [
            "-std=f2003",
            "-fall-intrinsics",
            "-fmax-identifier-length=63",
            "-ffree-line-length-132",
            "-fimplicit-none",
            "-fbounds-check",
            "-Warray-bounds",
            "-Werror",
            "-fopenmp",
        ]

    def fortran_compile_flags_override(self) -> dict[Path, list[str]]:
        return {
            Path("src/io/dump/read_dump_mod.F90"): self.fortran_compile_flags_common() + ["-fallow-argument-mismatch"],
        }
