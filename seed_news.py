import os
import django
import urllib.request

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()

from news.models import Author, Category, Article
from django.core.files import File

def download_image(url, filename):
    os.makedirs('media/news/images', exist_ok=True)
    filepath = os.path.join('media/news/images', filename)
    try:
        req = urllib.request.Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        with urllib.request.urlopen(req) as response, open(filepath, 'wb') as out_file:
            out_file.write(response.read())
        return filepath
    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None

def seed():
    Article.objects.all().delete()
    Author.objects.all().delete()
    Category.objects.all().delete()

    author1 = Author.objects.create(name='Sofía Martínez', email='sofia@globalnews.es', bio='Periodista especializada en Tecnología e Inteligencia Artificial.')
    author2 = Author.objects.create(name='Carlos Mendoza', email='carlos@globalnews.es', bio='Analista de Economía y Mercados Internacionales.')

    cat1 = Category.objects.create(name='Tecnología', slug='tecnologia', description='Últimas novedades sobre tecnología, IA y desarrollo de software.')
    cat2 = Category.objects.create(name='Ciencia', slug='ciencia', description='Descubrimientos científicos, exploración espacial e investigación.')
    cat3 = Category.objects.create(name='Economía', slug='economia', description='Mercados financieros, economía global y tendencias empresariales.')

    articles_data = [
        {
            'title': 'La Revolución de la Inteligencia Artificial en 2026',
            'slug': 'revolucion-inteligencia-artificial-2026',
            'author': author1,
            'category': cat1,
            'summary': 'Los sistemas autónomos multi-agente alcanzan nuevos hitos transformando la ingeniería de software y la automatización global.',
            'content': '<p>La Inteligencia Artificial ha transformado por completo el panorama tecnológico en este 2026. Los agentes autónomos son ahora capaces de ejecutar flujos de trabajo complejos con una precisión sin precedentes.</p><script>alert("Prueba XSS");</script><p><strong>Este texto en negrita y formato HTML se renderiza de forma segura gracias al filtro safe de Django.</strong> La adopción masiva de modelos avanzados optimiza la productividad en todos los sectores industriales.</p>',
            'image_url': 'https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=800&q=80',
            'img_name': 'ai_news.jpg'
        },
        {
            'title': 'Histórico Avance en Computación Cuántica',
            'slug': 'avance-computacion-cuantica',
            'author': author1,
            'category': cat2,
            'summary': 'Investigadores logran estabilidad en cúbits a temperatura ambiente, abriendo la puerta a procesadores comerciales.',
            'content': '<p>Un equipo internacional de físicos ha conseguido mantener una superposición cuántica estable a temperatura ambiente. Este descubrimiento elimina la necesidad de sistemas de refrigeración criogénica extremos, acercando la computación cuántica a los centros de datos comerciales.</p>',
            'image_url': 'https://images.unsplash.com/photo-1509228468518-180dd4864904?auto=format&fit=crop&w=800&q=80',
            'img_name': 'quantum_news.jpg'
        },
        {
            'title': 'Los Mercados Globales Cierran con Récord Histórico',
            'slug': 'mercados-globales-record-historico',
            'author': author2,
            'category': cat3,
            'summary': 'Las principales bolsas internacionales registran máximos históricos impulsadas por inversiones verdes.',
            'content': '<p>Los mercados bursátiles experimentaron un rally alcista masivo esta semana. Los fondos soberanos de inversión han incrementado notablemente sus asignaciones hacia infraestructuras de energía renovable y movilidad sostenible.</p>',
            'image_url': 'https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?auto=format&fit=crop&w=800&q=80',
            'img_name': 'markets_news.jpg'
        },
        {
            'title': 'El Futuro Brillante de las Energías Renovables',
            'slug': 'futuro-energias-renovables',
            'author': author1,
            'category': cat1,
            'summary': 'Las celdas solares de perovskita superan el 50% de eficiencia en pruebas de laboratorio.',
            'content': '<p>La nueva generación de paneles solares basada en perovskita ha roto todos los récords anteriores de eficiencia energética. Esto promete abaratar drásticamente el costo de la energía limpia para los hogares de todo el mundo.</p>',
            'image_url': 'https://images.unsplash.com/photo-1497435334941-8c899ee9e8e9?auto=format&fit=crop&w=800&q=80',
            'img_name': 'solar_news.jpg'
        },
        {
            'title': 'Asombrosos Descubrimientos en el Abismo Marino',
            'slug': 'descubrimientos-abismo-marino',
            'author': author2,
            'category': cat2,
            'summary': 'Biólogos marinos catalogan nuevas especies en fuentes hidrotermales del Océano Pacífico.',
            'content': '<p>Utilizando sumergibles autónomos avanzados, una expedición científica ha descubierto ecosistemas enteros prosperando alrededor de fuentes hidrotermales profundas, demostrando la increíble resiliencia de la vida.</p>',
            'image_url': 'https://images.unsplash.com/photo-1544551763-46a013bb70d5?auto=format&fit=crop&w=800&q=80',
            'img_name': 'ocean_news.jpg'
        },
        {
            'title': 'Nuevas Tendencias de Inversión en Startups',
            'slug': 'tendencias-inversion-startups',
            'author': author2,
            'category': cat3,
            'summary': 'El capital de riesgo redirige sus fondos hacia la tecnología profunda (deep tech) y biotecnología.',
            'content': '<p>Las firmas de capital de riesgo están alejándose de las aplicaciones de consumo masivo para apostar fuertemente por proyectos de ingeniería profunda, fusión nuclear y tratamientos biotecnológicos avanzados.</p>',
            'image_url': 'https://images.unsplash.com/photo-1522071820081-009f0129c71c?auto=format&fit=crop&w=800&q=80',
            'img_name': 'startup_news.jpg'
        },
    ]

    for data in articles_data:
        article = Article.objects.create(
            title=data['title'],
            slug=data['slug'],
            author=data['author'],
            category=data['category'],
            summary=data['summary'],
            content=data['content'],
            is_published=True
        )
        img_path = download_image(data['image_url'], data['img_name'])
        if img_path and os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                article.featured_image.save(data['img_name'], File(f), save=True)

    print("¡Imágenes reales de internet descargadas y asignadas a cada noticia exitosamente!")

if __name__ == '__main__':
    seed()
