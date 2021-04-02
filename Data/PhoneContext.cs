using Microsoft.EntityFrameworkCore;
using longhuu.Models;
namespace longhuu.Data
{
    public class PhoneContext : DbContext
    {
        public PhoneContext()
        {
        }
        public PhoneContext(DbContextOptions<PhoneContext> options): base(options)
        {
        }
        public DbSet<Phone> Phones { get; set; }
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            if (!optionsBuilder.IsConfigured)
            {
                optionsBuilder.UseSqlServer("Server=DESKTOP-3IAVUPL;Database=demo;Trusted_Connection=True;");
            }
        }
    }
}