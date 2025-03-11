/** 
 * This example is taken from the fmtlib README
 * https://github.com/fmtlib/fmt
**/
#include <fmt/chrono.h>
#include <fmt/ranges.h>
#include <vector>

int main() {
  auto now = std::chrono::system_clock::now();
  fmt::print("Date and time: {}\n", now);
  fmt::print("Time: {:%H:%M}\n", now);
  std::vector<int> v = {1, 2, 3};
  fmt::print("{}\n", v);
}