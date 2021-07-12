using API2PYTHON.Interfaces;
using API2PYTHON.Models;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;

namespace API2PYTHON.Managers
{
    public class ApiUrlMngr : IApiUrlMngr
    {
        #region Get Api url details
        public ApiUrlDetails GetApiUrlDeatils(string apiName)
        {
            //using (UnitOfWork<VerifIDContext> unitOfWork = new UnitOfWork<VerifIDContext>())
            //{
            //    using (GenericRepository<ParamConnApi> repository = new GenericRepository<ParamConnApi>(unitOfWork))
            //    {
            //        try
            //        {
            //            ParamConnApi paramObj = repository.Get(a => a.ApiConnName == apiName.ToUpper()).FirstOrDefault();
            //            return _mapper.Map<ApiUrlDetails>(paramObj);
            //        }
            //        catch (Exception ex)
            //        {
            //            _logs.ErrorLog(this.GetType().Name,
            //               MethodBase.GetCurrentMethod().Name,
            //               "Error for " + apiName,
            //               ex);
            //            return null;
            //        }
            //    }
            //}

            return null;
        }
        #endregion
    }


}
