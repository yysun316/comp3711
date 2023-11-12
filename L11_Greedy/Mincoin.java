import java.util.Vector;

class Mincoin {
    static int deno[] = { 1, 2, 5, 10, 20, 50, 100, 500, 1000 };
    static int n = deno.length;

    static Vector<Integer> findMin(int V) {
        Vector<Integer> ans = new Vector<>();

        for (int i = n - 1; i >= 0; i--) {
            while (V >= deno[i]) {
                V -= deno[i];
                ans.add(deno[i]);
            }
        }
        return ans;
    }

    static void print(Vector<Integer> arr) {
        for (int i = 0; i < arr.size(); i++)
            System.out.print(arr.elementAt(i) + " ");
        System.out.println();
    }

    public static void main(String[] args) {
        int n = 93;
        System.out.print("Following is minimal number of change for " + n + ": ");
        Vector<Integer> ans = findMin(n);
        print(ans);
    }
}