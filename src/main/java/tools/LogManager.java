package tools;

import java.io.IOException;
import java.util.logging.Logger;
import java.util.logging.Level;
import java.util.logging.FileHandler;
import java.util.logging.SimpleFormatter;

public class LogManager{
	private Logger logger;
	
	public LogManager(String logPath){
		logger = Logger.getLogger("BankLog");
		
		setFileHandler(logPath);
	}
	
	private void setFileHandler(String logPath){
		FileHandler fileHandler;
		try{
			fileHandler = new FileHandler(logPath);
			logger.addHandler(fileHandler);
			SimpleFormatter formatter = new SimpleFormatter();
			fileHandler.setFormatter(formatter);
		}catch (SecurityException e){
			e.printStackTrace();
		}catch (IOException e){
			e.printStackTrace();
		}
	}
	
	public void writeLog(Level level, String messageLog){
		if (level == Level.INFO){
			logger.info(messageLog);
		}
	}

	
}