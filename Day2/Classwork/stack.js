class Stack{
    constructor(){
        this.items=[];
    }
    push(element){
        this.items.push(element);
    }
    pop(){
        if (this.isEmpty()){
            return "Stack Empty";
        }
        return this.items.pop();
    }
    isEmpty(){
        return this.items.length===0;
    }
    peek(){
        if (this.isEmpty()){
            return "Stack Empty";
        }
        return this.items[this.items.length-1];
    }
    show(){
        console.log(this.items);
    }
}
const stack=new Stack();
stack.push(7);
stack.push(45);
stack.push(18);
stack.push(93);
console.log("on a peel into the items : "+stack.peek());
stack.show();
