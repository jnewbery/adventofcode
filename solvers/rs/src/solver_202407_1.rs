use std::collections::HashSet;

fn test_line(line: &str) -> i64 {
    let mut operands = line.split(|c: char| !c.is_numeric() && c != '-')
        .filter_map(|s| s.parse::<i64>().ok());
    let target = operands.next().unwrap();

    let mut results: HashSet<i64> = HashSet::new();
    results.insert(operands.next().unwrap());

    for operand in operands {
        let mut new_results = HashSet::new();
        for result in results.iter() {
            if result + operand <= target {
                new_results.insert(result + operand);
            }
            if result * operand <= target {
                new_results.insert(result * operand);
            }
        }
        results = new_results;
    }

    if results.contains(&target) {
        return target;
    }

    0
}

pub fn solve_202407_1(input: &str) -> String {
    let sol = input.lines().map(|line| test_line(line)).sum::<i64>();
    // println!("{:?}", sol);
    sol.to_string()
}