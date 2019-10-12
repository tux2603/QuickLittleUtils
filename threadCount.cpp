#include <iostream>
#include <thread>


int main() {
    std::cout << "This computer can run " << std::thread::hardware_concurrency() << " threads at a time" << std::endl;  
    return 0;
}