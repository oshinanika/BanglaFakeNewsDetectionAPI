using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace API2PYTHON.Models
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
