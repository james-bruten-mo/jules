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
    "openmp": True,
    "fortran_compile_flags_common": fortran_compile_flags_common + werror,
    "fortran_overrides": {
        Path("jules/src/io/dump/read_dump_mod.F90"): {
            "compile_flags": fortran_compile_flags_common + ["-fallow-argument-mismatch"],
        },
    },
    "fortran_pp_flags": ["-traditional", "-P"],
}
