package tools;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.HashMap;

public class ConfigFile{
	private HashMap<String, String> parameterMap = new HashMap<String, String>();
	
	public ConfigFile(String filename){
		String fileAsString = null;
		
		try{
			fileAsString = convertFileIntoString(filename);
		}catch(IOException io){
			io.printStackTrace();
		}
		
		String[] lines = fileAsString.split("\n");
		
		for(String currentLine : lines){
			addKeyToHashMap(currentLine.trim());
		}
	}
	
	private String convertFileIntoString(String filename) throws IOException{
		byte[] readFile = Files.readAllBytes(Paths.get(filename));
		return new String(readFile, StandardCharsets.UTF_8);
	}
	
	private void addKeyToHashMap(String lineToAdd){
		if(!lineToAdd.startsWith("#")){
			String[] keyAndValue = lineToAdd.split("=");
			if(keyAndValue.length == 2){
				parameterMap.put(keyAndValue[0].trim(), keyAndValue[1].trim());
			}
		}
	}
	
	public String get(String key){
		return parameterMap.get(key);
	}
}