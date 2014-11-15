package servlets;

import javax.servlet.http.HttpServlet;

import tools.ConfigFile;
import tools.LogManager;

public class Servlet extends HttpServlet{

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;
	
	protected ConfigFile configFile;
	protected LogManager logManager;
	
	public Servlet(ConfigFile configFile, LogManager logManager){
		this.configFile = configFile;
		this.logManager = logManager;
	}
	
}