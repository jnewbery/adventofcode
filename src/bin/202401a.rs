static _TEST_INPUT: &str = include_str!("202401_test_input.txt");
static _INPUT: &str = include_str!("202401_input.txt");

fn main() {
    // Parse lines into lists
    let mut lists: Vec<Vec<i32>> = vec![vec![], vec![]];
    _INPUT.lines().for_each(|line| {
        let parts: Vec<i32> = line
            .split_whitespace()
            .map(|s| s.parse::<i32>().expect("Failed to parse column"))
            .collect();
        lists[0].push(parts[0]);
        lists[1].push(parts[1]);
    });

    // Sort the lists
    lists.iter_mut().for_each(|inner_vec| inner_vec.sort());

    // Calculate the sum of absolute differences
    let sum: i32 = lists[0]
        .iter()
        .zip(lists[1].iter())
        .map(|(&a, &b)| (a - b).abs())
        .sum();

    println!("Sum: {:?}", sum);
}
