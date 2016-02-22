package net.marstone;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;

/**
 * Unit test for simple App.
 */
public class AppTest extends TestCase {
    
    /**
     * @return the suite of tests being tested
     */
    public static Test suite() {
        return new TestSuite( AppTest.class );
    }

    public void testMax1() {
        assertEquals(5, net.marstone.App.max(5, 5) );
    }

    public void testMax2() {
        assertEquals(5, net.marstone.App.max(3, 5) );
    }

    public void testMax3() {
        assertEquals(10, net.marstone.App.max(10, 6) );
    }


}
