# import java.util.Scanner;
#
# // 注意类名必须为 Main, 不要有任何 package xxx 信息
# public class Main {
#     public static void main(String[] args) {
#         Scanner in = new Scanner(System.in);
#         String a = in.next();
#         String b = in.next();
#         System.out.println(new Main().add(a, b));
#     }
#     public String add(String a, String b){
#         StringBuilder result=new StringBuilder();
#         int i=a.length()-1;
#         int j=b.length()-1;
#         int carry=0;
#         while(i>=0||j>=0||carry>0){
#             int sum=carry;
#             if(i>=0){
#                 sum+=a.charAt(i--)-'0';
#             }
#             if(j>=0){
#                 sum+=b.charAt(j--)-'0';
#             }
#             result.append(sum%2);
#             carry=sum/2;
#         }
#         return result.reverse().toString();
#     }
# }