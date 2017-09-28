use std::process::{Command, exit};

fn main() {
  let output = Command::new("./generate-grpc.sh")
    .output()
    .unwrap();

  print!("{}", String::from_utf8(output.stdout).unwrap());
  eprint!("{}", String::from_utf8(output.stderr).unwrap());
  exit(output.status.code().unwrap());
}
