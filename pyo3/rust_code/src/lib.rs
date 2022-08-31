
use pyo3::prelude::*;

#[pyfunction]
fn has_close_elements(numbers: Vec<f64>, threshold: f64) -> bool {
    for idx in 0..numbers.len() {
        for idx2 in 0..numbers.len() {
            if idx != idx2 {
                let distance = (numbers[idx] - numbers[idx2]).abs();
                if distance < threshold {
                    return true;
                }
            }
        }
    }

    return false;
}

/// A Python module implemented in Rust. The name of this function must match
/// the `lib.name` setting in the `Cargo.toml`, else Python will not be able to
/// import the module.
#[pymodule]
fn rust(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(has_close_elements, m)?)?;
    Ok(())
}
