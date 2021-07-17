using System;

namespace BanglaFakeNewsDetectionApp.Models
{

    public class NewsSet
    {
        public int articleID { get; set; }
        public string category { get; set; }
        public string content { get; set; }
        public DateTime date { get; set; }
        public string domain { get; set; }
        public string headline { get; set; }
        public int label { get; set; }
    }

}
