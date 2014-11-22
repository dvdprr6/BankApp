package server;

import java.io.IOException;


import web.WebServer;


public class StartServer{
	public static void main(String[] args){
		String configPath = System.getProperty("user.dir") + "/conf/dev/bank.conf";
		String logPath = System.getProperty("user.dir") + "/logs/server.log";
		
		WebServer webserver = new WebServer(configPath, logPath);

		webserver.start();
		
	}
}