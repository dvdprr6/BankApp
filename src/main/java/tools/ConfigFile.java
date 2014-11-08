package tools;

import java.lang.*;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;

public class ConfigFile{
	private HashMap<String, String> parameterMap;
	
	public ConfigFile(String filename) throws IOException{
		parameterMap = new HashMap<String, String>();
		
		byte[] readFile = Files.readAllBytes(Paths.get(filename));
		String fileAsString = new String(readFile, StandardCharsets.UTF_8);
		
		for(String currentLine : fileAsString.split("/n")){
			String trimCurrentLine = currentLine.trim();
			
			if(!trimCurrentLine.startsWith("#")){
				
			}
		}
	}
}