using System;

namespace BanglaFakeNewsDetectionApp.Models
{
    public class StatusResult<T>
    {
        public StatusResult()
        {
            Status = "FAILED";
            Message = "Something is Wrong";
        }

        public string Status;
        public string Message;
        public T Result;

        public static StatusResult<T> response(T data, string status, string message)
        {

            StatusResult<T> result = new StatusResult<T>();

            result.Result = data;
            result.Status = status;
            result.Message = message;

            return result;

        }
    }
}
