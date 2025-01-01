Uygulamamızın Amacı:
Amacımız kullanıcının istediği filmleri kendine ait özel bir listede tutabilmesi yorum yapabilmesi ve bu film ile ilgili bilgileri görüntüleyebilmesi
Uygulamamızın Kullanımı:
Uygulamamızı açar açmaz bizi ilk olarak kullanıcı adı ve şifre giriş ekranı karşılıyor. Üst kısımda yer alan filmler ve diziler seçeneği ile arşivimizde bulunan bütün film/diziler ile ilgili işlemler yapabiliyoruz. İstersek türüne göre filtreleyebilir istersek de bütün eserleri listeleyebiliriz. Sağ tarafta yer alan sekmeler aracılığı ile listelenen eserler hakkında bilgi sahibi olabilir eserlere yorum ve puan ekleyebilir bize öneri sunmasını isteyebilir veya istediğimiz eserleri listemize ekleyebiliriz. Bu eklemeleri istediğimiz anda değiştirebilir ve istediğimiz kadar liste oluşturabiliriz. 


Uygulamamızda kullandığımız fonksiyonlar:

create_login_page() :
Kullanıcıdan kullanıcı adı ve şifre bilgilerini alacak giriş yapma ekranı oluşturuyor. Yer alan giriş butonuna tıklayınca authenticate() fonksiyonunu çalıştırıyor.
authenticate() :
Kullanıcının girdiği bilgileri username ve password değişkenlerine atıyor. Eğer kullanıcı adı USERS içerisinde yer alıyorsa şu anki kullanıcı olarak belirleniyor ve kullanici_listeleri klasörü içerisinde yoksa kullanıcı için ayrı bir liste klasörü açılıyor. Ardından giriş mesajı oluşturup ana sayfayı oluşturacak olan create_main_page() fonksiyonu çalıştırılıyor.
create_main_page() :
Ana ekranımızı oluşturan fonksiyondur. Kullanıcının eylemleri sonucu programın çalışmasını sağlar.
switch_category() :
Ana ekranın üst kısmında yer alan butonlar sayesinde aktif olur. Aldığı değer movies ise üst kısımdaki yazıyı “Toplam Filmler: (sayısı)” eğer değilse “Toplam Diziler: (sayısı)” olarak değiştirir.  Ardından load_genres fonksiyonunu çalıştırır.
load_genres():
Sol çerçevede yer alan widget’ları temizliyor ardından film/dizi seçimine göre eserin türlerini gösterecek olan butonları ekliyor. Bu butonların özelliklerini belirleyen fonksiyonlara göndermeler yapıyor.
