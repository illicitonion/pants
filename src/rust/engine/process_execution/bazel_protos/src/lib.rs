#![feature(rust_2018_preview, uniform_paths)]

mod gen;
pub use crate::gen::*;

mod conversions;
mod verification;
pub use crate::verification::verify_directory_canonical;
