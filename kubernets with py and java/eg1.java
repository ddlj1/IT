public class AreaOfCircle {

    public static void main(String[] args){

        double radius = 5.0;

        if(args.length > 0){
            radius = Double.parseDouble(args[0]);
        }

        double area = Math.PI * Math.pow(radius,2);

        System.out.println("The area of circle with radius "
        + radius + " is: " + area);

        try{
            Thread.sleep(300000);
        }catch(Exception e){}
    }
}