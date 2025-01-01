Uygulamamızın Amacı:
Amacımız kullanıcının istediği filmleri kendine ait özel bir listede tutabilmesi yorum yapabilmesi ve bu film ile ilgili bilgileri görüntüleyebilmesi
Uygulamamızın Kullanımı:
Uygulamamızı açar açmaz bizi ilk olarak kullanıcı adı ve şifre giriş ekranı karşılıyor. Üst kısımda yer alan filmler ve diziler seçeneği ile arşivimizde bulunan bütün film/diziler ile ilgili işlemler yapabiliyoruz. İstersek türüne göre filtreleyebilir istersek de bütün eserleri listeleyebiliriz. Sağ tarafta yer alan sekmeler aracılığı ile listelenen eserler hakkında bilgi sahibi olabilir eserlere yorum ve puan ekleyebilir bize öneri sunmasını isteyebilir veya istediğimiz eserleri listemize ekleyebiliriz. Bu eklemeleri istediğimiz anda değiştirebilir ve istediğimiz kadar liste oluşturabiliriz. 


Uygulamamızda kullandığımız fonksiyonlar:
//EmreY
style_setup(self):
Uygulama içerisinde kullanılacak stili ayarlayan komuttur.
create_login_page(self) :
Kullanıcıdan kullanıcı adı ve şifre bilgilerini alacak giriş yapma ekranı oluşturuyor. Yer alan giriş butonuna tıklayınca authenticate() fonksiyonunu çalıştırıyor.
authenticate(self) :
Kullanıcının girdiği bilgileri username ve password değişkenlerine atıyor. Eğer kullanıcı adı USERS içerisinde yer alıyorsa şu anki kullanıcı olarak belirleniyor ve kullanici_listeleri klasörü içerisinde yoksa kullanıcı için ayrı bir liste klasörü açılıyor. Ardından giriş mesajı oluşturup ana sayfayı oluşturacak olan create_main_page() fonksiyonu çalıştırılıyor.
create_main_page(self) :
Ana ekranımızı oluşturan fonksiyondur. Kullanıcının eylemleri sonucu programın çalışmasını sağlar.
switch_category(self,category) :
Ana ekranın üst kısmında yer alan butonlar sayesinde aktif olur. Aldığı değer movies ise üst kısımdaki yazıyı “Toplam Filmler: (sayısı)” eğer değilse “Toplam Diziler: (sayısı)” olarak değiştirir.  Ardından load_genres fonksiyonunu çalıştırır.
load_genres(self):
Sol çerçevede yer alan widget’ları temizliyor ardından film/dizi seçimine göre eserin türlerini gösterecek olan butonları ekliyor. Bu butonların özelliklerini belirleyen fonksiyonlara göndermeler yapıyor.
add_review(self):
Herhangi bir öge seçilmediyse uyarı mesajı verip işlemini durduruyor. Eğer seçilen ögeler hakkında önceden yapılmış yorum varsa o bilgilerle beraber bir pencere açıyor. Kullanıcı bu bilgileri güncelleyebilir/değiştirebilir. Girilen bilgiler kontrol edildikten sonra herhangi bir problem yoksa json dosyasına kaydediliyor.
random_recommendation():
Öneri bekleniyor mesajı veriyor. 2 saniyelik bir beklemenin ardından seçilen eserin türü ve genresine göre rastgele bir eser seçip bize eser ile ilgili bilgilerin yer aldığı bir mesaj kutusu gösteriyor.

//Simay
show_lists(self):
Kullanıcının mevcut listelerini gösteren yeni bir pencere açar. Listelere çift tıklayarak içeriğini görüntüleyebilir. 
show_list_content(self, list_name): 
Seçilen listenin içeriğini yükler ve görüntüler. İçerik, bir tablo formatında sunulur; bu sayede kullanıcılar listelerinin detaylarını görebilir. 
clear_window(self):
Mevcut penceredeki tüm widget'ları temizler. Yeni içerik yüklenmeden önce kullanılmak üzere bir yardımcı fonksiyondur. 
load_genres(self):
Sol çerçevede bulunan tür butonlarını doldurur. Mevcut filmler veya dizilerden türleri alır ve butonlar oluşturur; bu sayede kullanıcılar belirli türlerdeki içeriklere kolayca erişebilir. 
filter_data(self, data): 
Geçersiz girişleri filtreler; belirli kriterlere uymayan film veya dizileri hariç tutar. Bu işlem, yalnızca geçerli verilerin görüntülenmesini sağlar.
