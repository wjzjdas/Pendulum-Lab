import java.util.*;

class test1{
    
    public static void main(String arg[]){
        
        Scanner scan = new Scanner(System.in);

       System.out.println(RNG(scan.nextInt()));
       scan.close(); 
        
       
    }
    
    public static int RNG(int i){
        return ((int)(Math.random()*i+1));
    }
}