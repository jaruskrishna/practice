public class ReverseString {
    public static void main(String[] args) {
        String text = "hello";
        String reversed = reverse(text);

        System.out.println("Original string: " + text);
        System.out.println("Reversed string: " + reversed);
    }

    public static String reverse(String text) {
        StringBuilder reversed = new StringBuilder();

        for (int i = text.length() - 1; i >= 0; i--) {
            reversed.append(text.charAt(i));
        }

        return reversed.toString();
    }
}
