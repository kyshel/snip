package com.example.helloworld;


public class A {

    void func1(String s1) {
        System.out.println(s1);
    }

    public static void main(String[] args) {


        A a1 = new A();
        a1.func1("asdbdbsb");

    }










    void permutation(String str) {
        permutation(str, "");

    }
    void permutation(String str, String prefix) {
        if (str.length() == 0) {
            System.out.println(prefix);
        } else {
            for (int i= 0; i < str.length(); i++) {
                String rem = str.substring(0, i) + str.substring(i + 1);
                permutation(rem, prefix + str.charAt(i));
            }
        }
    }







}
