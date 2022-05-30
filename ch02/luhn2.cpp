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
 *         Author:  Matt Simpson
 *   Organization:
 *
 * =====================================================================================
 */

#include <iostream>
using std::cin;
using std::cout;

int getDigit(){

  char digit;

  digit = cin.get();

  if(digit == 10){
    return 0;
  }

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
  int oddsum = 0;
  int evensum = 0;
  int position = 1;
  int checksum;

  cout << "Enter a number: ";

  digit = getDigit();

  while(digit != 0){
    if(position % 2 == 0){
      oddsum += doubleDigitValue(digit);
      evensum += digit;
    } else {
      oddsum += digit;
      evensum += doubleDigitValue(digit);
    }
    digit = getDigit();
    position++;
  }

  if((position - 1) % 2 == 0){
    checksum = evensum;
  } else {
    checksum = oddsum;
  }

  cout << "Checksum is: " << checksum << ".\n";

  return 0;
}
