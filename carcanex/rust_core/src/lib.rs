use pyo3::prelude::*;
use serde::{Deserialize, Serialize};

#[pyclass]
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct CanFrame {
    #[pyo3(get, set)]
    pub timestamp: f64,
    #[pyo3(get, set)]
    pub arbitration_id: u32,
    #[pyo3(get, set)]
    pub data: Vec<u8>,
}

#[pymethods]
impl CanFrame {
    #[new]
    fn new(timestamp: f64, arbitration_id: u32, data: Vec<u8>) -> Self {
        CanFrame {
            timestamp,
            arbitration_id,
            data,
        }
    }
}

#[pyfunction]
fn parse_raw_frame(raw_data: Vec<u8>) -> PyResult<CanFrame> {
    // This is a stub for high-performance parsing logic
    // Implementation would go here
    Ok(CanFrame {
        timestamp: 0.0,
        arbitration_id: 0,
        data: raw_data,
    })
}

#[pymodule]
fn carcanex_core(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<CanFrame>()?;
    m.add_function(wrap_pyfunction!(parse_raw_frame, m)?)?;
    Ok(())
}
