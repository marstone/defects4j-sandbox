package net.marstone;

/**
 * Hello world!
 *
 */
public class App  {
	public static void main( String[] args ) {
		System.out.println( App.max(3, 5) );
		System.out.println( "Hello World!" );
	}

	public static int max(int x, int y) {
		// the FIX version, should be '>'
		if(x > y) {
			return x;
		} else {
			return y;
		}
	}


}
