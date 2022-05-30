/*
 * =====================================================================================
 *
 *       Filename:  halfsquare.cpp
 *
 *    Description:
 *
 *
 *        Version:  1.0
 *        Created:  08/10/2021 05:14:29 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  Matt Simpson
 *   Organization:
 *
 * =====================================================================================
 */

#include <iostream>
using std::cin;
using std::cout;

int main(){
  for(int row = 1; row <= 8; row++){
    for(int hashNum = 1; hashNum <= 4 - abs((4 - row)); hashNum++){
      cout << "#";
    }

    cout << "\n";
  }

  return 0;
}
