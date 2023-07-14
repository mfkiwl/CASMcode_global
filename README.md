The libcasm-global package
==========================

The `libcasm-global` package provides generically useful tools used by CASM:

- CASM global constants and definitions
- Input / output tools, especially for JSON parsing and formatting
- An Eigen distribution and methods
- Helpers for runtime library compiling and linking
- Miscellaneous mathematical functions
- etc.


Install from source
===================

Installation of `libcasm-global` requires:
- Python >=3.8
- Standard compilers:
  - On Ubuntu linux:

      sudo apt-get install build-essential

  - On Mac OSX, install Command Line Tools for XCode:

      xcode-select --install


Normal installation:

    pip install .


Building documentation
======================

Install documentation requirements:

    pip install -r doc_requirements.txt

Install `libcasm-global` first, then build and open the documentation:

    cd python/doc
    make html
    open _build/html/index.html


Testing
=======

To install testing requirements, do:

    pip install -r test_requirements.txt

Use `pytest` to run the tests. To run all tests, do:

    python -m pytest -rsap python/tests

As an example of running a specific test, do:

    python -m pytest -rsap python/tests/test_prim.py::test_asymmetric_unit_indices


Developing
==========

To install development requirements, do:

    pip install -r dev_requirements.txt

[TODO] Building is performed using scikit-build to help create distributions that include both the C++ and Python portions of CASM, which are linked using pybind11. Using the standard build process, editable installation of the pure Python components is not supported by scikit-build or scikit-build-core (the next generation of scikit-build), but may be possible soon. In the meantime, for development of Python components, editable installation can be done by first installing the pure C++ portion of CASM with the cmake option `CASM_CXX_ONLY` and then installing the pybind11 wrapper and Python portions of CASM. The following is an example developing in a conda environment where the C++ library is installed in `$CONDA_PREFIX`:

    # make and install CASM C++ library only:
    mkdir build_cmake_cpp_only
    cd build_cmake_cpp_only
    cmake -DCMAKE_INSTALL_PREFIX=$CONDA_PREFIX -DCASM_CXX_ONLY=ON ..
    make -j4 VERBOSE=1
    make -j4 test
    make install

    # use the setup.py in CASMcode_global/python/ for editable install:
    cd ../python
    pip install -e .


Known issues
------------

See [Known Issues](https://scikit-build.readthedocs.io/en/latest/index.html#known-issues) for scikit-build:

- The cache directory (_skbuild) may need to be deleted between builds in some cases (like rebuilding with a different Python interpreter).


Formatting
----------

For Python code formatting, use black. Do:

    black .

For C++ code formatting, use clang-format with `-style=google`. Use the `stylize.sh` script to format files staged for commit. To enforce that it is run before committing, place the `pre-commit` file, or equivalent code, in `.git/hooks`. After `git add` do:

    # git add <new and changed files>
    ./stylize.sh
    # git add <formatted new and changed files>
    # check changes and commit

When C++ files have been added or removed from `include/`, `src/`, or `tests/`, then `CMakeLists.txt` may be updated from the `CMakeLists.txt.in` template using:

      python make_CMakeLists.py

Adding tests
------------

Python:
- Add Python tests for `libcasm.<subpackage>` in `python/tests/<subpackage>`, using pytest.
- If data files are needed for testing, they can be placed in `python/tests/<subpackage>/data/`.
- To access data files use the `shared_datadir` fixture available from the [`pytest-datadir`](https://pypi.org/project/pytest-datadir/) plugin.
- To create temporary testing directories for reading and writing files, use the [`tmpdir` and `tmpdir_factory`](https://docs.pytest.org/en/7.4.x/how-to/tmp_path.html#the-tmpdir-and-tmpdir-factory-fixtures) fixtures available from pytest.
- For tests that involve an expensive setup process, such as compiling Clexulators, a session-length shared datadir can be constructed once and re-used as done [here](https://github.com/prisms-center/CASMcode_clexulator/blob/2.X/python/tests/clexulator/conftest.py) in CASMcode_clexulator.
- Expensive tests can also be set to run optionally using flags as demonstrated in CASMcode_clexulator.

C++:
- Add C++ library tests in `tests/unit/<module>`, with the naming convention `<something>_test.cpp`, using googletest.
- If data files are needed for testing, they can be placed in `tests/unit/<module>/data/`.
- To access data files and create temporary testing directories for reading and writing files, use the methods available in `tests/unit/testdir.hh`.
- If a new module is added, (i.e. a new `casm/<module>`) then new unit tests should be added under `tests/unit/<module/` and `tests/CMakeLists.txt.in` and `make_CMakeLists.py` must be updated to add the new unit tests.
- To run only C++ library tests, follow the example for building only the C++ library.


Creating distributions
----------------------

To create a source distribituion do:

    python -m build --sdist

To create a wheel do:

    python -m build --wheel
