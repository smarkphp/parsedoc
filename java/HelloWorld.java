package com.company.test;

/**
 * @ClassName HelloWorld
 * @Description TODO
 * @Author mark1117
 * @Date 2020/10/4 - 3:26 下午
 */
public class HelloWorld {

    public static int sum(int a, int b) {
        int c = a + b;
        return c;
    }

    public static void main(String[] args){
        int cv = sum(4,5);
        System.out.println(cv);
    }
}
