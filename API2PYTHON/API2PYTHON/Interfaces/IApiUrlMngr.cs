using API2PYTHON.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace API2PYTHON.Interfaces
{
    public interface IApiUrlMngr
    {
        public ApiUrlDetails GetApiUrlDeatils(string apiName);
    }
}
