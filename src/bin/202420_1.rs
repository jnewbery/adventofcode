static TEST: bool = true;

static _TEST_INPUT: &str = include_str!("inputs/202420_test.txt");
static _INPUT: &str = include_str!("inputs/202420.txt");

const INPUT: &str = if TEST { _TEST_INPUT } else { _INPUT };

fn main() {
    println!("{}", INPUT);
}