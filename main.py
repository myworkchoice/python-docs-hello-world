using System;
using System.Collections.Generic;
using System.IO;
using System.Net.Http;

namespace PackageUploader.Azure
{
    public class AzureStorageApi
    {
        public void UploadFile(String fullFilePath, String blobSasUri, Dictionary<String, String> metadata = null)
        {
            using (var client = new HttpClient())
            using (var fileStream = File.OpenRead(fullFilePath))
            {
                HttpContent content = new StreamContent(fileStream);
                content.Headers.Add("x-ms-blob-type", "BlockBlob");
                foreach (var pair in metadata ?? new Dictionary<string, string>())
                {
                    content.Headers.Add("x-ms-meta-" + pair.Key, pair.Value);
                }
                var response = client.PutAsync(blobSasUri, content).Result;
                if (response.IsSuccessStatusCode)
                {
                    return;
                }
                var exceptionMessage = String.Format("Unable to finish request. Server returned status: {0}; {1}", response.StatusCode, response.ReasonPhrase);
                throw new ApplicationException(exceptionMessage);
            }
        }
    }
}
