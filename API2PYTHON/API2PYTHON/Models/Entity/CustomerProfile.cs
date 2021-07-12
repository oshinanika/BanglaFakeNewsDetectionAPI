using System;
using System.Collections.Generic;
//using VerifID.Models.Security;
using System.ComponentModel;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
using System.Linq;
using System.Threading.Tasks;

namespace API2PYTHON.Models.Entity
{

        [Table("CUSTOMER_PROFILES")]
        public partial class CustomerProfile
        {
            public CustomerProfile()
            {
               // CustomerBenifOwner = new HashSet<CustomerBenifOwner>();
               // CustomerNominee = new HashSet<CustomerNominee>();
               // CustomerDocuments = new HashSet<CustomerDocument>();

               // NomineeGuardian = new HashSet<NomineeGuardian>();
               // FatkaAnswer = new HashSet<FatkaAnswer>();
               // ParamCusAdditionalInfoDtls = new HashSet<ParamCusAdditionalInfoDtls>();


            }
            [Key]
            [Required]
            [Column("TRACKING_NO", Order = 0)]
            public int TrackingNo { get; set; }

            [Column("MOBILENO", Order = 3)]
            [MaxLength(20)]
            public string? MobileNo { get; set; } = string.Empty;

            [Column("EMAIL", Order = 4)]
            [MaxLength(100)]
            public string? Email { get; set; } = string.Empty;
            [Column("FULLNAMEEN", Order = 7)]
            [MaxLength(100)]
            public string? FullnameEN { get; set; } = string.Empty;

            [Column("OTPSMS", Order = 9)]
            [MaxLength(20)]
            public string? OtpSms { get; set; } = string.Empty;
            [MaxLength(20)]
            [Column("OTPEMAIL", Order = 10)]
            public string? OtpEmail { get; set; } = string.Empty;

            [Column("NAME_OF_ORG", Order = 15)]
            [MaxLength(105)]
            [DefaultValue("")]
            public string? NameOfOrg { get; set; }

            //[Required]
            //[Column("MAKEBY", Order = 150)]
            //[MaxLength(30)]
            //public string MakeBy { get; set; }
            [Required]
            [Column("MAKEDT", Order = 151)]

            public DateTime MakeDt { get; set; }

            //public virtual CustomerRiskGrade CustomerRiskGrade { get; set; }
            
        
      

           // public virtual CustomerTimeAcMast CustomerTimeAcMast { get; set; }
            



        
        }
    }
