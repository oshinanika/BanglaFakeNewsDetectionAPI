using Microsoft.EntityFrameworkCore;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using API2PYTHON.Models.Entity;

namespace API2PYTHON.Models.Context
{
    public class AppDBContext : DbContext 
    {
        public AppDBContext(DbContextOptions<AppDBContext> options)
           : base(options)
        {
        }

        public virtual DbSet<CustomerProfile> CustomerProfiles { get; set; }
        public virtual DbSet<CustomerOtp> CustomerOtps { get; set; }

    }
}
