from pathlib import Path

fortran_compile_flags_common =[
    "-fall-intrinsics",
    "-std=f2003",
    "-fmax-identifier-length=63",
    "-ffree-line-length-132",
    "-fimplicit-none",
    "-fbounds-check",
    "-Warray-bounds",
]

werror = ["-Werror"]

compile_profile = {
    "min_compiler_version": "12",
    "fortran_compile_flags_common": fortran_compile_flags_common + werror,
    "fortran_compile_flags_override": {
        Path("src/io/dump/read_dump_mod.F90"): fortran_compile_flags_common + ["-fallow-argument-mismatch"]
    },
    "openmp": True,
}
