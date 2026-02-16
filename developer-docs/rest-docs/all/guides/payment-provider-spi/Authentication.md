SortOrder: 2
# Authentication

Follow the instructions in [Validating Requests Received From Wix](https://devforum.wix.com/en/article/validating-requests-received-from-wix).

> **Note**:  
When performing this operation it's important to use a raw request body.
Do not parse the request to JSON as it will not save the properties' order and it may break your validation.

## Header in cURL examples
In all examples for the SPI the header will hold a JSON web token (JWT) with the signed data:
```
-H 'Digest: <WIX-JWT-SIGNATURE>' 
```

## Example in Java
This code uses `jose4j` for JWT implementation.
```xml
<dependency>
    <groupId>org.bitbucket.b_c</groupId>
    <artifactId>jose4j</artifactId>
    <version>0.7.0</version>
</dependency>
``` 
Code to check is under `isWixRequest` method.
```java
package com.wix.provider.example;

import org.jose4j.jwt.MalformedClaimException;
import org.jose4j.jwt.consumer.InvalidJwtException;
import org.jose4j.jwt.consumer.JwtConsumer;
import org.jose4j.jwt.consumer.JwtConsumerBuilder;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import javax.xml.bind.DatatypeConverter;
import java.nio.charset.StandardCharsets;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.PublicKey;
import java.util.HashMap;
import java.util.Map;

public class JwtVerifier {
    private Logger logger = LoggerFactory.getLogger(JwtVerifier.class);
    private JwtConsumer jwtConsumer;

    public JwtVerifier(PublicKey key) {
        this.jwtConsumer = new JwtConsumerBuilder().setVerificationKey(key)
                .setRequireIssuedAt()
                .setRequireExpirationTime()
                .build();
    }

    public Boolean isWixRequest(String requestRawBody, String jwtToken) {
        try {
            Map<String, String> data = jwtConsumer.processToClaims(jwtToken).getClaimValue("data", HashMap.class);
            return data.keySet().stream().findFirst().map(hashFunction -> checkHashedBody(requestRawBody, data, hashFunction)).get();
        } catch (InvalidJwtException e) {
            logger.error("Invalid JWT signature", e);
        } catch (MalformedClaimException e) {
            logger.error("Invalid JWT data format", e);
        }
        return false;
    }

    private Boolean checkHashedBody(String requestRawBody, Map<String, String> data, String hashFunction) {
        try {
            byte[] digest = MessageDigest.getInstance(getHashFunctionName(hashFunction)).digest(requestRawBody.getBytes(StandardCharsets.UTF_8));
            return DatatypeConverter.printHexBinary(digest).equalsIgnoreCase(data.get(hashFunction));
        } catch (NoSuchAlgorithmException e) {
            logger.error("Unsupported hash algorithm", e);
        }
        return false;
    }

    private String getHashFunctionName(String value) {
        if (value.equalsIgnoreCase("SHA256")) return "SHA-256";
        else return "";
    }
}
```
