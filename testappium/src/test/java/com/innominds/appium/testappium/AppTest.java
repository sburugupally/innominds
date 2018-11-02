package com.innominds.appium.testappium;

import java.net.MalformedURLException;
import java.net.URL;
import java.util.concurrent.TimeUnit;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.remote.DesiredCapabilities;
import org.testng.annotations.BeforeMethod;

import io.appium.java_client.android.AndroidDriver;
import io.appium.java_client.remote.MobileCapabilityType;

/**
 * Unit test for simple App.
 */
public class AppTest 
  	
{
DesiredCapabilities capabilities = new DesiredCapabilities();
	
	@org.testng.annotations.Test
	public void Capbality() throws MalformedURLException {
		capabilities.setCapability(MobileCapabilityType.DEVICE_NAME, "4e50cab6");
		capabilities.setCapability(MobileCapabilityType.PLATFORM_NAME, "Android");
		capabilities.setCapability(MobileCapabilityType.PLATFORM_VERSION, "6.0.1");
//		capabilities.setCapability(MobileCapabilityType.APP, "C:\\Users\\statipamula\\AppData\\Local\\Android\\Sdk\\tools\\emulator.exe");
		capabilities.setCapability("noReset", true);
		capabilities.setCapability("fullReset", false);
		capabilities.setCapability("appPackage", "com.google.android.gm");
		capabilities.setCapability("appActivity", ".ConversationListActivityGmail");
			
		String appium_url = "http://localhost:4723/wd/hub";
		AndroidDriver driver = new AndroidDriver(new URL(appium_url),capabilities);
		driver.manage().timeouts().implicitlyWait(30,TimeUnit.SECONDS);

		WebElement compose_button = driver.findElement(By.id("com.google.android.gm:id/compose_button"));
		compose_button.click();
//		  // Click on DELETE/CLR button to clear result text box before running test.
//		   driver.findElements(By.id("com.instagram.android:id/avatar_image_view"));
//
//		  // Click on number 2 button.
//		  driver.findElement(By.name("7")).click();
		   
		}
}