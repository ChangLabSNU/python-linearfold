# python-linearfold

Unofficial CPython binding to LinearFold

### Installation

Use `pip` to install the module.

```bash
pip install linearfold-unofficial
```

You may build from the source code for unsupported Python versions or platforms.

```bas
git clone --recursive https://github.com/ChangLabSNU/python-linearfold
cd python-linearfold
pip install .
```

### Usage

The module currently only has one function called `fold(seq)`, and
it doesn't have any customizable options other than the defaults.
The seq parameter should be an RNA sequence in *uppercase* letters,
and any `T` should be converted to `U` before passing it to the function.

```python
>>> import linearfold
>>> seq = 'UGUCGGGUAGCUUAUCAGACUGAUGUUGACUGUUGAAUCUCAUGGCAACACCAGUCGAUGGGCUGUCUGACA'
>>> linearfold.fold(seq)
('((((((((((((((((.(((((.(((((.(((.(((...))))))))))).)))))))))))))))))))))', -34.6)
```

The function returns a tuple with two elements. The first element
is the predicted MFE structure, and the second element is the free
energy of the structure in kcal/mol.

### Author

Hyeshik Chang &lt;hyeshik@snu.ac.kr&gt;

### License

This Python binding is licensed under [the MIT-style license](LICENSE).
However, the compiled binary includes code from the LinearFold
package, which is licensed for non-commercial use.
