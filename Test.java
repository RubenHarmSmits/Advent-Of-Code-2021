import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Scanner;

public class Test {
	int totalRow = 5;
	char[][] grid = new char[totalRow][];
	char[][] key = {{'0','0','0','0','0','0','0'},{'0','0','0','1','0','0','0'},{'0','0','2','3','4','0','0'},{'0','5','6','7','8','9','0',},{'0','0','A','B','C','0','0'},{'0','0','0','D','0','0','0'},{'0','0','0','0','0','0','0'}};
	int x = 1;
	int y = 3;
	File file = new File("input.txt");
	Scanner scanner = new Scanner(file);

	public Test() throws FileNotFoundException {

	}


	public static void main(String[] args) throws FileNotFoundException {
		System.out.println("Testing");
		new Test().solve();
	}

	void solve() {
		makeGrid();
		ArrayList<Character> ans = new ArrayList<>();
		for(char[] line:grid) {
			//System.out.println(line);
			ans.add(getCode(line));
		}
		System.out.println(ans);
	}

	char getCode(char[] line){
		for(char c:line){
			switch(c){
				case 'U': {
					if(key[y-1][x]!='0')y--;
				}
				break;
				case 'D': {
					if(key[y+1][x]!='0')y++;
				}
				break;
				case 'L': {
					if(key[y][x-1]!='0')x--;
				}
				break;
				case 'R': {
					if(key[y][x+1]!='0')x++;
				}
				break;
			}

		}
		char ruben = key[y][x];
		//System.out.println("ruben:"+ruben);
		return ruben;

	}

	void makeGrid(){
		for (int row = 0; scanner.hasNextLine() && row < totalRow; row++) {
			grid[row] = scanner.nextLine().toCharArray();
		}
	}
}
