#![feature(rust_2018_preview, uniform_paths)]
extern crate bytes;
extern crate futures;
extern crate grpcio;
extern crate hashing;
extern crate protobuf;

mod gen;
pub use crate::gen::*;

mod conversions;
mod verification;
pub use crate::verification::verify_directory_canonical;
