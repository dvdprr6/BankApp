package web;

import java.io.IOException;
import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.util.logging.Level;

import javax.servlet.Servlet;

import tools.ConfigFile;
import tools.LogManager;

import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.server.ServerConnector;
import org.eclipse.jetty.server.handler.ContextHandler;
import org.eclipse.jetty.server.handler.ContextHandlerCollection;
import org.eclipse.jetty.server.handler.ResourceHandler;
import org.eclipse.jetty.servlet.ServletContextHandler;
import org.eclipse.jetty.servlet.ServletHolder;

public class WebServer{
	private ConfigFile config;
	private Server server;
	private LogManager logManager;
	private ContextHandlerCollection contextHandlerCollection;

	
	public WebServer(String configPath, String logPath){
		config = new ConfigFile(configPath);
		logManager = new LogManager(logPath);
		
		//logManager = new LogManager(currentClass, logPath);
		
		String host = config.get("server.host");
		int port = Integer.parseInt(config.get("server.port"));
		
		initializeServer(host, (short)port);
	}
	
	private void initializeServer(String host, short port){
		server = new Server();
		contextHandlerCollection = new ContextHandlerCollection();
		server.setHandler(contextHandlerCollection);
		
		ServerConnector http = new ServerConnector(server);
		http.setHost(host);
		http.setPort(port);
		http.setIdleTimeout(30000);
		server.addConnector(http);
		
		ResourceHandler resourceHandler = new ResourceHandler();
		resourceHandler.setDirectoriesListed(true);
		resourceHandler.setWelcomeFiles(new String[] {"index.html"});
		resourceHandler.setResourceBase(System.getProperty("user.dir") + "/" + config.get("server.www.path"));
		
		ContextHandler contextHandler = new ContextHandler("/");
		contextHandler.setContextPath("/");
		contextHandler.setHandler(resourceHandler);
		contextHandlerCollection.addHandler(contextHandler);
	}
	
	public void addServlet(Class<? extends Servlet> servletClass, String servletName) throws NoSuchMethodException, SecurityException, InstantiationException, IllegalAccessException, IllegalArgumentException, InvocationTargetException{
		Constructor<?> constructor = servletClass.getConstructor(ConfigFile.class, LogManager.class);
		Servlet servlet = (Servlet)constructor.newInstance(config, logManager);
		
		ServletContextHandler servletContextHandler = new ServletContextHandler();
		servletContextHandler.setContextPath(servletName);
		servletContextHandler.addServlet(new ServletHolder(servlet), "/");
		contextHandlerCollection.addHandler(servletContextHandler);
	}
	
	public void start(){
		try{
			server.start();
			logManager.writeLog(Level.INFO, "Webserver started version (=Beta)");
			server.join();
		}catch (Exception e){
			e.printStackTrace();
		}
		//logManager.writeLog(Level.INFO, "WebServer starter version(=1.0)");
	}

}