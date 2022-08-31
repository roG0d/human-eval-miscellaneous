fn main(){
let mut v1: Vec<i32> = Vec::new();

for i in 0..5 {
    let b = i.clone();
    v1.push(b);
}

println!("{:?}",v1);
}