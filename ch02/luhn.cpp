/*
 * =====================================================================================
 *
 *       Filename:  luhn.cpp
 *
 *    Description:
 *
 *        Version:  1.0
 *        Created:  08/10/2021 06:28:32 PM
 *       Revision:  none
 *       Compiler:  gcc
 *
 *         Author:  YOUR NAME (),
 *   Organization:
 *
 * =====================================================================================
 */

#include <iostream>
using std::cin;
using std::cout;

int getDigit(){
  char digit;

  cout << "Enter a single digit number (0-9): ";
  digit = cin.get();

  digit = digit - '0';

  return digit;
}

int doubleDigitValue(int digit){

  int doubledDigit = digit * 2;
  int sum;

  if(doubledDigit >= 10){
    sum = 1 + (doubledDigit % 10);
  }
  else{
    sum = doubledDigit;
  }

  return sum;
}

int main(){
  char digit;
  int sum;

  digit = getDigit();

  sum = doubleDigitValue(digit);

  cout << "Sum of digits in doubled number: " << sum << "\n";

  return 0;
}
