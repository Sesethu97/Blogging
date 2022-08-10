interface Test {
    test(): void;
    test2(): string;
}

class HelloWorld implements Test {
    test(): void {
        console.log("test");
    }
    
    test2(): string {
        return "hello";
    }

    static main(args: string[]): void {
        console.log("Hello World");
    }
}

HelloWorld.main([]);